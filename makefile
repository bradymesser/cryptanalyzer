default:
	python3 HW1code_Brady_Messer.py inputText.txt

run:
	python3 HW1code_Brady_Messer.py aliceCh4.txt
	mv output.txt aliceCh4Output.txt
	python3 HW1code_Brady_Messer.py aliceCh8.txt
	mv output.txt aliceCh8Output.txt

clean:
	rm output.txt aliceCh4Output.txt aliceCh8Output.txt dcOut.txt

decrypt:
	python3 decrypt.py inputText.txt

translate:
	python3 translate.py inputText.txt
