import dropbox

class TransferData :

    def __init__(self, access_token):
            self.access_token = access_token

    def upload_file(self, file_from, file_to):
            """upload a file to Dropbox using API v2
            """
            dbx = dropbox.Dropbox(self.access_token)

            f = open(file_from, 'rb')
            dbx.files_upload(f.read(), file_to)

    def main():
        access_token = 'sl.A9wo2wQy4IgQq6ouQFSLWElL-hch-JQLF9pvdQSPzThIU7AQvFWflM0NQxcT_QTT78nYBqgaIjpcsnURfa8sfZ8gCdDYWETIiYM_9993XOSWV3wOgl9SbNYVmg0Eewxg_aAbeT0'
        transferData = TransferData(access_token)

        file_from = input("Enter the path of file to transfer the file")
        file_to = '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages'
        # API v2
        transferData.upload_file(file_from, file_to)
        print('the file is transfered')
        
    main()
