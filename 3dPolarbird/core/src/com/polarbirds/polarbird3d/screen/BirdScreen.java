package com.polarbirds.polarbird3d.screen;

import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.g3d.ModelBatch;
import com.badlogic.gdx.math.Vector3;
import com.polarbirds.polarbird3d.model.Bird;

/**
 * Created by Kristian Rekstad on 18.12.2015.
 */
public class BirdScreen implements Screen {

    public static final int MINIMUM_VIEWPORT_SIZE = 20; // Unit: blocks
    public static final int CAMERA_DEGREES_PER_SECOND = 36;

    private PerspectiveCamera camera;
    private ModelBatch modelBatch;

    private Bird bird;

    private final Vector3 cameraTarget = new Vector3(0, 10, 0);

    @Override
    public void show() {
        camera = new PerspectiveCamera(67, 32, 20);
        modelBatch = new ModelBatch();

        camera.position.set(0, 15, 25);
        camera.lookAt(cameraTarget);
        camera.update();

        bird = new Bird();

    }

    @Override
    public void render(float delta) {
        camera.position.rotate(Vector3.Y, delta * CAMERA_DEGREES_PER_SECOND);
        camera.lookAt(cameraTarget);
        camera.up.set(Vector3.Y);
        camera.update();

        modelBatch.begin(camera);
        //modelBatch.render(floor);
        modelBatch.render(bird);
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

        bird.dispose();
        bird = null;
    }
}
