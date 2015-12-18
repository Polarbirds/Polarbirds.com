package com.polarbirds.polarbird3d.desktop;

import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;
import com.polarbirds.polarbird3d.MainGame;

public class DesktopLauncher {
    public static void main (String[] arg) {
        LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
        config.vSyncEnabled = true;
        config.backgroundFPS = 4;
        config.samples = 4;

        new LwjglApplication(new MainGame(), config);
    }
}
