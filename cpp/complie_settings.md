# Compile settings

[solution](https://stackoverflow.com/questions/39091173/how-to-enable-c17-on-mac)

VS Code -> settings `command + ,` -> Code-runner: Executor map -> settings.json -> `"cpp": "cd $dir && g++ --std=c++2a $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"`