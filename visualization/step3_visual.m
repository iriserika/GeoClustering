clc
clear 
close all

fid = fopen('../data/lat_longs');
C = textscan(fid, '%f %f %s', 'Delimiter', ' ');
fclose(fid);

latitude = C{1};
longitude = C{2};

plot(longitude, latitude, 'x');
xlabel('Longitude');
ylabel('Latitude');
grid on;
title('Visualization of DBpedia Location Data');

fid = fopen('../data/lat_longs_small');
C = textscan(fid, '%f %f %s', 'Delimiter', ' ');
fclose(fid);

latitude = C{1};
longitude = C{2};

plot(longitude, latitude, 'x');
xlabel('Longitude');
ylabel('Latitude');
grid on;
title('Visualization of DBpedia Location Data Filtered in US');