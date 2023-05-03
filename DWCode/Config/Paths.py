		echo "GITHUB_WORKSPACE: $GITHUB_WORKSPACE"
		python --version
		echo "Step 1: Installing schemachange"
		pip install schemachange
		echo "Step 2: Running schemachange " 
	
		schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Functions        -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Procedures       -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Tables           -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Claims/Views            -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Functions      -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Procedures     -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Tables         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Medication/Views          -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Functions     -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Procedures    -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Tables        -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Organization/Views         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Functions          -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Procedures         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Tables             -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Patient/Views              -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/Common_Utility              -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Functions     -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Procedures    -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Tables        -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac
		schemachange -f $GITHUB_WORKSPACE/DWCode/CareTeam/Views         -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE -c $SF_DATABASE.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table -ac