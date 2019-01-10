from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute

class qrng ():
    
    def __init__( self, precision=64, num = 100 ):
        
        self.precision = precision
        self.num = num
        
        q = QuantumRegister(1)
        c = ClassicalRegister(1)
        qc = QuantumCircuit(q,c)
        qc.h(q)
        qc.measure(q,c)
        job = execute(qc,backend=Aer.get_backend('qasm_simulator'),shots=precision*num,memory=True)
        data = job.result().get_memory()
        
        self.int_list = []
        n = 0
        for _ in range(num):
            bitstring = ''
            for b in range(precision):
                bitstring += data[n]
                n += 1
            self.int_list.append( int(bitstring,2) )
            
        self.n = 0
        
    def rand_int(self):
        
        rand_int = self.int_list[self.n]
        
        self.n = self.n+1 % self.num
        
        return rand_int
    
    def rand(self):
        
        rand_float = self.int_list[self.n] / 2**self.precision
        
        self.n = (self.n+1) % self.num
        
        return rand_float