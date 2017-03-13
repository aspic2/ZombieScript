# ZombieScript
Tool for Google's DFP API. Returns Line Item info from a provided list of LIDs.

Natively in DFP, it is impossible to get bulk Line Item info unless the lines in question 
have a common grouping (e.g., same advertiser, same order, etc.). This application allows you to
search for a list of unrelated line items and return information about them in a spreadsheet.

The name comes from the Zombie Report, a monthly report that my ad serving team completes.
Our inventory team gives us a list of lines that are not running, but are taking up inventory.
Now, rather than inspecting each one individually, we can run this app to return that info.



# Requirements
The script is in Python 3, and it requires a few packages before use. 
  - googleads
  - openpyxl

# Instructions
After downloading the project and installing the prerequisite packages:
- Place your excel file with a column of LIDs in the sourcefiles folder.
    - Update the file path for variable 'source_wb' within main.py
- Add a path to your authentication file (.yaml) to the variable 'auth_file' within main.py
- Update sourceLIDs in main() of main.py to the Excel column hosting your LIDs
- Run the script and wait for your info.

LineItemInfo.txt shows every attribute that can be returned from the request.
There are more notes in the source file if you need to customize this app more.

# Licenses
This application is a derivative of googleads' get_all_line_items.py, under Apache License.
Beyond their licensing rules, I grant permission to use, edit, and distribute my project as
desired.

-MT
