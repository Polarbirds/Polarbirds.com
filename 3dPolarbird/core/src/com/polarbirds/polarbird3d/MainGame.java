package com.polarbirds.polarbird3d;

import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.polarbirds.polarbird3d.screen.BirdScreen;

public class MainGame extends Game {

    @Override
    public void create () {
        setScreen(new BirdScreen());
    }

    @Override
    public void render () {
        Gdx.gl.glClearColor(0.4f, 0.4f, 0.4f, 0.f);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT | GL20.GL_DEPTH_BUFFER_BIT);
        super.render();
    }

    @Override
    public void dispose() {
        super.dispose();
        getScreen().dispose();
        setScreen(null);
    }

}
