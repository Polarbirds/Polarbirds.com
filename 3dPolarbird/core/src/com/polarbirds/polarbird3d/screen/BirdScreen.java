package com.polarbirds.polarbird3d.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.VertexAttributes;
import com.badlogic.gdx.graphics.g3d.*;
import com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute;
import com.badlogic.gdx.graphics.g3d.loader.ObjLoader;
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder;
import com.badlogic.gdx.math.Vector3;

/**
 * Created by Kristian Rekstad on 18.12.2015.
 */
public class BirdScreen implements Screen {

    public static final int MINIMUM_VIEWPORT_SIZE = 15; // Unit: blocks

    private PerspectiveCamera camera;
    private ModelBatch modelBatch;

    private Model bird;
    private ModelInstance birdInstance;
    private ModelInstance floorInstance;

    private final Vector3 cameraTarget = new Vector3();

    @Override
    public void show() {
        camera = new PerspectiveCamera(67, 25, 15);
        modelBatch = new ModelBatch();

        cameraTarget.set(0, 7, 0);

        camera.position.set(0, 10, 20);
        camera.lookAt(cameraTarget);
        camera.update();

        ModelBuilder builder = new ModelBuilder();

        Material floorMaterial = new Material(ColorAttribute.createDiffuse(0.1f, 0.1f, 0.1f, 1.f));

        Model floorModel = builder.createBox(12, 1, 12, floorMaterial,
                VertexAttributes.Usage.Position
                        | VertexAttributes.Usage.ColorPacked
                        | VertexAttributes.Usage.Normal);
        floorInstance = new ModelInstance(floorModel, 0, 0, 0);

        ObjLoader loader = new ObjLoader();

        bird = loader.loadModel(Gdx.files.internal("model/bird.obj"));
        birdInstance = new ModelInstance(bird);
    }

    @Override
    public void render(float delta) {
        camera.position.rotate(Vector3.Y, delta*36);
        camera.lookAt(cameraTarget);
        camera.up.set(Vector3.Y);
        camera.update();

        modelBatch.begin(camera);
        modelBatch.render(floorInstance);
        modelBatch.render(birdInstance);
        modelBatch.end();
    }

    @Override
    public void resize(int width, int height) {
        if (width > height) {
            camera.viewportHeight = MINIMUM_VIEWPORT_SIZE;
            camera.viewportWidth = camera.viewportHeight * (float)width / (float)height;
        } else {
            camera.viewportWidth = MINIMUM_VIEWPORT_SIZE;
            camera.viewportHeight = camera.viewportWidth * (float)height / (float)width;
        }
        camera.update();
    }

    @Override
    public void pause() {

    }

    @Override
    public void resume() {

    }

    @Override
    public void hide() {

    }

    @Override
    public void dispose() {
        modelBatch.dispose();
        camera = null;

        floorInstance = null;
    }
}
