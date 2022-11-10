import wx
from event import EventEmitter, EVENT_UPDATE_LIST

class ATMPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl = wx.ListCtrl(
            self, 
            size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )

        self.list_ctrl.InsertColumn(0, "Customer turn", width=140)
        self.list_ctrl.InsertColumn(1, "Num transactions", width=140)

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        
        close_button = wx.Button(self, label="Close")
        close_button.Bind(wx.EVT_BUTTON, self.close)

        main_sizer.Add(close_button, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    
    def close(self, event):
        quit()

    def update_customer_list(self, customers):
        self.list_ctrl.DeleteAllItems()
        for index, customer in enumerate(customers):
            self.list_ctrl.InsertItem(index, customer.id_number)
            self.list_ctrl.SetItem(index, 1, str(customer.num_transac))


class ATMFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(parent=None, title="ATM")

        self.panel = ATMPanel(self)
        self.Show()


class ATMUI():
    
    def start(self):
        app = wx.App()

        self.frame = ATMFrame()

        EventEmitter.subscribe(EVENT_UPDATE_LIST, self.update_customer_list)

        app.MainLoop()

    def update_customer_list(self, customers):
        self.frame.panel.update_customer_list(customers)

