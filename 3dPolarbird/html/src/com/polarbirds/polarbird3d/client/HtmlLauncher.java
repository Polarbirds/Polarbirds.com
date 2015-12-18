package com.polarbirds.polarbird3d.client;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.backends.gwt.GwtApplication;
import com.badlogic.gdx.backends.gwt.GwtApplicationConfiguration;
import com.polarbirds.polarbird3d.MainGame;

public class HtmlLauncher extends GwtApplication {

    @Override
    public GwtApplicationConfiguration getConfig () {
        final GwtApplicationConfiguration gwtApplicationConfiguration = new GwtApplicationConfiguration(480, 320);
        gwtApplicationConfiguration.antialiasing = true;
        gwtApplicationConfiguration.alpha = true;

        return gwtApplicationConfiguration;
    }

    @Override
    public ApplicationListener getApplicationListener () {
        return new MainGame();
    }
}