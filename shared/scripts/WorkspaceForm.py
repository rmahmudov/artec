source(findFile("scripts", "BaseForm.py"))

class WorkspaceForm(BaseForm):
    item = "{class='wxWindowClassNR' text='wxdataviewctrlmainwindow' type='WindowsControl'}"

    def __init__(self):
        super(WorkspaceForm, self).__init__("{class='wxWindowClassNR' text='workspace' type='WindowsControl'}","Панель 'Workspace'")
    
    def select(self,num=1):
        mouseClick(waitForObject(self.item),48,12*num, MouseButton.LeftButton)
        
    def performContextMenuItemAction(self,action,num=1):
        mouseClick(waitForObject(self.item),48,12*num, MouseButton.RightButton)
        mouseClick(waitForObject(":%s_MenuItem"%action))