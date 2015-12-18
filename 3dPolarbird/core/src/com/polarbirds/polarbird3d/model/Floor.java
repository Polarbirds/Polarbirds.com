package com.polarbirds.polarbird3d.model;

import com.badlogic.gdx.graphics.VertexAttributes;
import com.badlogic.gdx.graphics.g3d.*;
import com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute;
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.Disposable;
import com.badlogic.gdx.utils.Pool;

/**
 * Created by Kristian Rekstad on 19.12.2015.
 */
public final class Floor implements RenderableProvider, Disposable {

    private static Model floor;
    private static int floorRefCount = 0;
    private final ModelInstance floorInstance;

    public Floor() {
        if (floor == null){
            ModelBuilder builder = new ModelBuilder();

            Material floorMaterial = new Material(ColorAttribute.createDiffuse(0.1f, 0.1f, 0.1f, 1.f));

            Model floorModel = builder.createBox(12, 1, 12, floorMaterial,
                    VertexAttributes.Usage.Position
                            | VertexAttributes.Usage.ColorPacked
                            | VertexAttributes.Usage.Normal);
        }

        floorRefCount++;
        floorInstance = new ModelInstance(floor, 0, 0, 0);
    }

    @Override
    public void dispose() {
        if (--floorRefCount == 0){
            floor.dispose();
            floor = null;
        }
    }

    @Override
    public void getRenderables(Array<Renderable> renderables, Pool<Renderable> pool) {
        floorInstance.getRenderables(renderables, pool);
    }
}
