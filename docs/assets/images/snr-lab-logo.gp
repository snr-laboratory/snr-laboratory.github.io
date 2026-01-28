# Logo for the SNR-Lab.org site.
set output "snr-lab-logo.svg"
set term svg size 640,480 dynamic lw 2

unset zeroaxis
unset xlabel
unset ylabel
unset tics
unset border
unset key

set xrange [-3*pi:3*pi]
set yrange [-2.8:0.1]
#set log y

sinc(x)=sin(x)/x
clip(x)=x**2/200.0
s(x)=log10(sinc(x)**2/2.0)
f(x)=(s(x)>clip(x)-3.0)?s(x):1/0

set samples 100
# reset rand seed
print rand(-1)

plot f(x) w l lw 10 lc "red", log10(1.0+rand(0)/5.0)-clip(x) w l lw 5 lc "web-blue"

unset output
