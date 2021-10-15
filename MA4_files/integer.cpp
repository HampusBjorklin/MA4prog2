#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
	private:
		int val;
		int fibonacci(int);
	};
 
Integer::Integer(int n){
	val = n;
	}


int Integer::fibonacci(int n){
   if (n <= 1){
    return n;
   }
   else{
    return fibonacci(n-1)+ fibonacci(n-2);
   }
}


int Integer::get(){
	return val;
	}

void Integer::set(int n){
	val = n;
	}

int Integer::fib(){
    return fibonacci(val);
}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	int Integer_fib(Integer* integer) {return integer ->fib();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}