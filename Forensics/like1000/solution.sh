tar -xf 1000.tar
for i in {999..1}; do
	tar -xf $i.tar
	rm $i.tar
done

# picoCTF{l0t5_0f_TAR5}
