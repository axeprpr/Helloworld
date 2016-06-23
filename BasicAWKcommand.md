#####Duplicate removal
```
awk '{!a[$0]++}'
```
Derivative:
```
awk '{!a[$1]+=3}'
```
This will keep three multiple values in the first column. 
##### Change the value of the specific domain
```
awk 'BEGIN{FS=OFS="|";}$1~/ABC/{gsub(DEF/,"GHI",$3)}1' FILENAME.txt 1<>FILENAME.txt
```
