@echo off

REM プロジェクト内の全てのPythonファイルを再帰的に検索してPylintでチェック

for /r awssample %%f in (*.py) do (
    pylint "%%f"
)
pause