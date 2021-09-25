from timeit import default_timer as timer
import time, base64
 
def block_miner(text, digits):
    import hashlib
    n = 0
    m = ''
    ntext = text
    
    while hashlib.sha256(ntext.encode('utf-8')).hexdigest()[0:digits] != "0"*digits:
        n +=1
        b = bytes(str(n), "ascii")
        m = base64.b64encode(b).decode('utf-8')
        ntext = f'{text}{m}'
    
    return(text, m , n, hashlib.sha256(ntext.encode("utf-8")).hexdigest())
 
if __name__ == '__main__':
    ZEROS_REQUIRED = 12
    for i in range(0, ZEROS_REQUIRED + 1):
         
        start = time.perf_counter() 
        name, iters, attempts, hash = block_miner("45363809", i)   
        end = time.perf_counter()  
         
        print(f'{name} {iters:10} Tries:{attempts} in {end-start:7.4f} seconds => {hash}')
