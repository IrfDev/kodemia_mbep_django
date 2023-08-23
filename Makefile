SHELL=/bin/bash


dev: 
	./start_dev.sh 

install:
	./install.sh $(package)

today:
	@./activate_env.sh

finish:
	./finish_day.sh -m "$(message)"