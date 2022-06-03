function Y=my_dct(X)
X=double(X);
[m,n]=size(X);
A = zeros(m);   
for i = 0:m-1
    for j = 0:n-1
        if i == 0
            a = sqrt(1/m);
        else
            a = sqrt(2/m);
        end
        A(i+1,j+1) = a*cos((j+0.5)*pi*i/m);
    end
end
Y=A*X*A';