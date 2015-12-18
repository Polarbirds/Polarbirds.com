package com.polarbirds.polarbird3d.screen;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.VertexAttributes;
import com.badlogic.gdx.graphics.g3d.*;
import com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute;
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder;
import com.badlogic.gdx.math.Vector3;

/**
 * Created by Kristian Rekstad on 18.12.2015.
 */
public class BirdScreen implements Screen {

    public static final int MINIMUM_VIEWPORT_SIZE = 7; // Unit: blocks

    private PerspectiveCamera camera;
    private ModelBatch modelBatch;

    private Model bird;
    private ModelInstance birdInstance;
    private ModelInstance floorInstance;

    @Override
    public void show() {
        camera = new PerspectiveCamera(67, 12, 7);
        modelBatch = new ModelBatch();

        camera.position.set(0, 5, 12);
        camera.lookAt(Vector3.Zero);
        camera.update();

        ModelBuilder builder = new ModelBuilder();

        Material floorMatierial = new Material(ColorAttribute.createDiffuse(0.1f, 0.1f, 0.1f, 1.f));

        Model floorModel = builder.createBox(12, 1, 12, floorMatierial,
                VertexAttributes.Usage.Position
                        | VertexAttributes.Usage.ColorPacked
                        | VertexAttributes.Usage.Normal);
        floorInstance = new ModelInstance(floorModel, 0, 0, 0);
    }

    @Override
    public void render(float delta) {
        camera.position.rotate(Vector3.Y, delta*36);
        camera.lookAt(Vector3.Zero);
        camera.up.set(Vector3.Y);
        camera.update();

        modelBatch.begin(camera);
        modelBatch.render(floorInstance);
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
