.PHONY: build-pb
build-pb:
	mkdir -p pb
	protoc -Iproto --python_out=pb $$(find proto -name '*.proto')