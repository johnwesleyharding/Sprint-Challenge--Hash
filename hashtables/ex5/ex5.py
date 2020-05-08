def finder(files, queries):
    
    ht = {}
    result = []
    
    for file in files:
        
        tail = file.split('/')[-1]
        
        if tail in ht:
            
            ht[tail].append(file)
            
        else:
            
            ht[tail] = [file]
    
    for query in queries:
        
        if query in ht:
            
            result += ht[query]

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
