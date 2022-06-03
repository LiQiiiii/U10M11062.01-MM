function Y=ex3(X)
mask=[1 1 1 1 1 0 0 0
      1 1 1 1 0 0 0 0
      1 1 1 0 0 0 0 0
      1 1 0 0 0 0 0 0
      0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0;];
X=double(X);
A = zeros(8);   
for i = 0:7
    for j = 0:7
        if i == 0
            a = sqrt(1/8);
        else
            a = sqrt(2/8);
        end
        A(i+1,j+1) = a*cos((j+0.5)*pi*i/8);
    end
end
 Y=X.*mask;