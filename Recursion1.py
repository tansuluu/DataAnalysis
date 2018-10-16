def recur_partial(text):
    if len(text)>0:
        print(text[1:]);
        recur_partial(text[1:]);
        
        
