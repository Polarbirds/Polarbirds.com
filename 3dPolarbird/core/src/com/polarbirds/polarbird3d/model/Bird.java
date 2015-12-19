package com.polarbirds.polarbird3d.model;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.ModelInstance;
import com.badlogic.gdx.graphics.g3d.Renderable;
import com.badlogic.gdx.graphics.g3d.RenderableProvider;
import com.badlogic.gdx.graphics.g3d.loader.G3dModelLoader;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.Disposable;
import com.badlogic.gdx.utils.Pool;
import com.badlogic.gdx.utils.UBJsonReader;

/**
 * Created by Kristian Rekstad on 19.12.2015.
 */
public final class Bird implements RenderableProvider, Disposable {

    private static Model bird;
    private static int birdRefCount = 0;
    private final ModelInstance birdInstance;

    public Bird() {
        if (bird == null){
            G3dModelLoader loader = new G3dModelLoader(new UBJsonReader());
            bird = loader.loadModel(Gdx.files.internal("model/bird.g3db"));
        }

        birdRefCount++;
        birdInstance = new ModelInstance(bird);
    }

    @Override
    public void dispose() {
        if (--birdRefCount == 0){
            bird.dispose();
            bird = null;
        }
    }

    @Override
    public void getRenderables(Array<Renderable> renderables, Pool<Renderable> pool) {
        birdInstance.getRenderables(renderables, pool);
    }
}
