# 3D Polarbird

This subproject is intented to be a small project to get some content on [Polarbirds.com](http://www.polarbirds.com).
It's purpose is to display the bird logo in 3D, using [libGDX](https://libgdx.badlogicgames.com/) and [GWT](http://www.gwtproject.org/).

## Getting started

We use IntelliJ and Gradle. Open the <code>.ipr</code> file after cloning.
Add VCS root, import gradle projects, and configure GWT when prompted by IntelliJ.

## Running

See [Running your project](https://github.com/libgdx/libgdx/wiki/Gradle-and-Intellij-IDEA#running-your-project) for more details.
Run via gradle, with <code>gradlew</code> for Linux/OSX, and <code>gradlew.bat</code> for Windows.
Use the terminal (<code>View > Tool Windows > Terminal</code>).
Alternatively use the Gradle tool window in IntelliJ (<code>View > Tool Windows > Gradle</code>).

To run the desktop version, use <code>gradlew desktop:run</code>.

To run the html version, use <code>gradlew html:superDev</code>, 
and open [localhost:8080/html](http://localhost:8080/html/) when it reports:
```
The code server is ready.      
Next, visit: http://localhost:9876/
> Building 91% > :html:superDev
```
Ignore <code>91%</code> and <code>9876/</code>. It's really <code>100%</code> and <code>8080/html</code>. 
Stop with <code>Ctrl+C</code>. 
