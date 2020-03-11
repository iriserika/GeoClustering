clc
clear 
close all

load sample_geo.txt

latitude = sample_geo(:,1);
longitude = sample_geo(:,2);

plot(longitude, latitude, 'x');
xlabel('Longitude');
ylabel('Latitude');
grid on;
title('Visualization of Synthetic Location Data');