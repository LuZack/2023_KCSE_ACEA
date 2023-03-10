@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  app startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%..

@rem Add default JVM options here. You can also use JAVA_OPTS and APP_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\lib\app.jar;%APP_HOME%\lib\client-3.0.0.jar;%APP_HOME%\lib\gen.jdt-3.0.0.jar;%APP_HOME%\lib\gen.python-3.0.0.jar;%APP_HOME%\lib\gen.c-3.0.0.jar;%APP_HOME%\lib\core-3.0.0.jar;%APP_HOME%\lib\simmetrics-core-3.2.3.jar;%APP_HOME%\lib\guava-31.1-jre.jar;%APP_HOME%\lib\commons-csv-1.9.0.jar;%APP_HOME%\lib\commons-collections4-4.4.jar;%APP_HOME%\lib\org.eclipse.jgit-6.0.0.202111291000-r.jar;%APP_HOME%\lib\failureaccess-1.0.1.jar;%APP_HOME%\lib\listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar;%APP_HOME%\lib\jsr305-3.0.2.jar;%APP_HOME%\lib\checker-qual-3.12.0.jar;%APP_HOME%\lib\error_prone_annotations-2.11.0.jar;%APP_HOME%\lib\j2objc-annotations-1.3.jar;%APP_HOME%\lib\classindex-3.10.jar;%APP_HOME%\lib\fastutil-8.3.1.jar;%APP_HOME%\lib\gson-2.8.2.jar;%APP_HOME%\lib\jgrapht-core-1.5.1.jar;%APP_HOME%\lib\org.eclipse.jdt.core-3.26.0.jar;%APP_HOME%\lib\JavaEWAH-1.1.13.jar;%APP_HOME%\lib\slf4j-api-1.7.30.jar;%APP_HOME%\lib\commons-codec-1.10.jar;%APP_HOME%\lib\jheaps-0.13.jar;%APP_HOME%\lib\org.eclipse.core.resources-3.18.100.jar;%APP_HOME%\lib\org.eclipse.text-3.12.300.jar;%APP_HOME%\lib\org.eclipse.core.expressions-3.8.200.jar;%APP_HOME%\lib\org.eclipse.core.runtime-3.26.100.jar;%APP_HOME%\lib\org.eclipse.core.filesystem-1.9.500.jar;%APP_HOME%\lib\org.eclipse.core.jobs-3.13.200.jar;%APP_HOME%\lib\org.eclipse.core.contenttype-3.8.200.jar;%APP_HOME%\lib\org.eclipse.equinox.app-1.6.200.jar;%APP_HOME%\lib\org.eclipse.equinox.registry-3.11.200.jar;%APP_HOME%\lib\org.eclipse.equinox.preferences-3.10.100.jar;%APP_HOME%\lib\org.eclipse.core.commands-3.10.300.jar;%APP_HOME%\lib\org.eclipse.equinox.common-3.17.0.jar;%APP_HOME%\lib\org.eclipse.osgi-3.18.200.jar;%APP_HOME%\lib\org.osgi.service.prefs-1.1.2.jar;%APP_HOME%\lib\osgi.annotation-8.0.1.jar

@rem Execute app
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %APP_OPTS%  -classpath "%CLASSPATH%" kcse_acea.Main %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable APP_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%APP_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
