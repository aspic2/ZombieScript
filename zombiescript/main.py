# DFP Tool: Reads a list of LIDs from an excel sheet and returns specified
# data about the lines.
#
# Additional Info:
# Writing queries:
# https://developers.google.com/doubleclick-publishers/docs/pqlreference
# https://github.com/googleads/googleads-python-lib/blob/master/googleads/dfp.py


# Import appropriate modules from the client library.
from googleads import dfp
from googleads import errors

from Spreadsheet import Spreadsheet
from os import getcwd


#enter path to authentication file (.yaml file)
auth_file = getcwd() + "\\SourceFiles\\googleads.yaml"

#put your source workbook in the sourcefiles folder
#specify the filename at the end of path below
source_wb = getcwd() + "\\SourceFiles\\YOUR_SOURCE_FILE.xlsx"


def main(client):
    old_workbook = Spreadsheet('old_workbook', False, source_wb)
    new_workbook = Spreadsheet('ZReport', True)
    #set this to the column you want read (the one with LIDs)
    sourceLIDs = old_workbook.read('F')
    #query requires LIDs as a string starting and ending with quotes, e.g.:
    #'(555555, 555556, 555557)'
    sourceLIDs = tuple(sourceLIDs)
    sourceLIDs = str(sourceLIDs)

    # Initialize DFP service.
    line_item_service = client.GetService('LineItemService', version='v201702')

    # More info on customizing your query in the links at top
    query = ('WHERE id IN ' + sourceLIDs)

    # Create a statement to select line items.
    statement = dfp.FilterStatement(query)

    while True:
        response = line_item_service.getLineItemsByStatement(statement.ToStatement(
        ))
        if 'results' in response:
            for line_item in response['results']:
                # for more tuple value options, see LineItemInfo.txt
                token = (line_item['id'], line_item['name'],
                line_item['status'], line_item['isMissingCreatives'])
                new_workbook.append(token)
            statement.offset += dfp.SUGGESTED_PAGE_LIMIT
        else:
            break
        new_workbook.save()
    print('\nNumber of results found: %s' % response['totalResultSetSize'])

if __name__ == '__main__':
    # Initialize client object.
    dfp_client = dfp.DfpClient.LoadFromStorage(auth_file)
    main(dfp_client)
