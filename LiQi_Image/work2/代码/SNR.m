function snr=SNR(I,In)
Ps=sum(sum(I.^2));
Pn=sum(sum((In-I).^2));
snr=Ps/Pn;