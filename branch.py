import grpc
import banks_pb2
import banks_pb2_grpc
from concurrent import futures

class Branch(banks_pb2_grpc.BanksServicer):
    def __init__(self, id, balance, branches):
        self.id = id
        self.balance = balance
        self.branches = branches
        self.recvMsg = list()    # list to store received response
        self.stubList = list()   # list to store stubs for propagation
        self.branch2Stub = {} # a map to store branch to stub
        
    # students are expected to store the processID of the branches  
    def createStub(self): 
        for branchId in self.branches:  
            if branchId != self.id:  # creating a stub except itself for propagation
                port = str(50000 + branchId)
                channel = grpc.insecure_channel("localhost:" + port)  
                stub = banks_pb2_grpc.BanksStub(channel)
                self.stubList.append(stub)
                self.branch2Stub[branchId] = stub 
    
    def MsgDelivery(self, request, context):
        if request.interface == "query":
            result = self.Query()
            return banks_pb2.MsgResponse(balance=result)
        
        if request.interface == "deposit":
            result = self.Deposit(request.money)
            if result == "success":
                self.propagate("propagate_deposit", request.money)

        elif request.interface == "withdraw":
            result = self.Withdraw(request.money)
            if result == "success":
                self.propagate("propagate_withdraw", request.money)

        elif request.interface == "propagate_deposit":
            result = self.Propagate_Deposit(request.money)

        elif request.interface == "propagate_withdraw":
            result = self.Propagate_Withdraw(request.money)
        
        return banks_pb2.MsgResponse(result=result)
    
    def Query(self):
        return self.balance     
            
    def Deposit(self, money):   
        self.balance += money
        self.recvMsg.append({"interface": "deposit", "money": money})
        return "success"

    def Withdraw(self, money): 
        if self.balance < money:
            return "fail" 
        
        self.balance -= money
        self.recvMsg.append({"interface": "withdraw", "money": money})  
        return "success"
    
    def propagate(self, action, money):
        for branchId in self.branches:
            if branchId != self.id:
                stub = self.branch2Stub.get(branchId)
                stub.MsgDelivery(banks_pb2.MsgRequest(interface=action, money=money))

    def Propagate_Deposit(self, money):  
        self.balance += money
        return "success"

    def Propagate_Withdraw(self, money):  
        self.balance -= money
        return "success"

