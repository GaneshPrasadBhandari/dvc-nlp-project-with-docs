# echo [$(date)]: "START"
# echo [$(date)]: "creating environment"
# conda create --prefix ./env python=3.7 -y
# echo [$(date)]: "activate environment"
# source activate ./env
# echo [$(date)]: "install requirements"
# pip install -r requirements.txt
# echo [$(date)]: "END"

# # to remove everything -
# # rm -rf env/ .gitignore conda.yaml README.md .git/

echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create --p ./env python=3.8 -y
echo [$(date)]: "activate environment"
conda activate ./env/
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "END"