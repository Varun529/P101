import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.accessToken)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    accessToken="FJ_IF3jBrsoAAAAAAAAAAVVkrOUY2BIdKGSUav5p4kfEARLlWzYgqh0o2KMlhimK"
    transferdata=TransferData(accessToken)
    
    file_from=input("Enter the source path")
    file_to=input("Enter the destination path")
    
    transferdata.uploadFile(file_from,file_to)
    print("File has been moved")


if __name__=="__main__":
    main()