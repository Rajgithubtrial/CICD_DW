name: dev_path
# Controls when the action will run
on:
  push:
    branches: []

jobs:
  deploy-path:
    runs-on: ubuntu-latest
    environment: 'Dev'
    
    steps:
      #- name: Checkout repository
       # uses: actions/checkout@v2
        
      - name: Run schemachange for Dev
        env:
            SF_ACCOUNT: ${{ secrets.DEV_SF_ACCOUNT }}
            SF_USERNAME: ${{ secrets.DEV_SF_USERNAME }}
            SF_ROLE: ${{ secrets.DEV_SF_ROLE }}
            SF_WAREHOUSE: ${{ secrets.DEV_SF_WAREHOUSE }}
            SF_DATABASE: ${{ secrets.DEV_SF_DATABASE }}
            SNOWFLAKE_PASSWORD: ${{ secrets.DEV_SF_PASSWORD }}       
            run: |
               echo "GITHUB_WORKSPACE: $GITHUB_WORKSPACE"
  #python $GITHUB_WORKSPACE/Paths.py 
        #shell: sh 
          
           #python --version
           #echo "Step 1: Installing schemachange"
           #pip install schemachange
           #echo "Step 2: Running schemachange " 


#	schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Functions        -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Procedures       -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Tables           -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Views            -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Functions      -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Procedures     -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Tables         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Views          -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Functions     -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Procedures    -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Tables        -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Views         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Functions          -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Procedures         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Tables             -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Views              -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/Common_Utility              -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Functions     -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Procedures    -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Tables        -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
#	schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Views         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
