str_sum(str1,str2){
    if(len(str1)<len(str2)):
        swap(str1,str2)
    m=len(str1)
    n=len(str2)
    string=""

    car=0;
    for i in range(0,n):
        ds=((str1[m-1-i]-'0')+(str2[n-1-i]-'0')+car)%10
        car=((str1[m - 1 - i] - '0') +(str2[n - 1 - i] - '0') +car) / 10
        string=ch(car(ds+'0')+string
  
