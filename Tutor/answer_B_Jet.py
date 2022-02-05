a = int(input("Enter a : "))
r = int(input("Enter r : "))
p = int(input("Enter p : "))
n = int(input("Enter n : "))

def power_p(base, power):
	p = 1
	for i in range(power):
		p = p*base
	return p

sum_s  = 0
temp = 0
if n==0:
	result = a
else:
	for i in range(1, n+1):
		temp = a + i*r
		sum_s = sum_s + power_p(temp, p)
	result = sum_s+a

print(f"Result: {sum_s}")


# out put
10 9 8 7 6 5 4 3 2 1 0
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5 
10 9 8 7 6
10 9 8 7
10 9 8

# mst 

a
a-b
a-b-i
a-b-i-d
a-b-i-d-k
a-b-i-c-d-k
a-b-i-c-d-k-e


a
a-b
a-b-i
a-b-i-c
a-b-i-n-c
a-b-i-n-k-c
a-b-i-n-k-h-c

a
a-b
a-b-i
a-b-i-c
a-b-i-n-c
a-b-i-n-k-c
h-a-b-i-n-k-c


# linked list

struct node {
	double data;
	node *next;
}

int main() {
	struct node *head;
	head = malloc(sizeof(struct node))
	struct node *temp = head;
	struct node *temp_t, *temp_next;
	while(temp->next != head) {
		temp_next = temp->next
		if(temp->data > temp_next->data) {
			temp_t->data = temp->data;
			temp->data = temp_next->data;
			temp_next->data = temp_t->data;
		}
		temp = temp->next
	}

}

struct node {
    double data;
    node *next;
}

int main() {
    struct node *head;
    head = malloc(sizeof(struct node))
    struct node *temp = head;
    struct node *temp_t, *temp_next;
    while(temp->next != head) {
        temp_next = t  emp->next
        if(temp->data > temp_next->data) {  
            temp_t->data = temp->data;
            temp->data = temp_next->data;
            temp_next->data = temp_t->data;
        }
        temp = temp->next
    }

}



# padma bridge toll system:

Class pay_info{
		 Platinum = 10
	Gold = 8
Silver = 5
}
Class payment(payinfo){   // inheritance
Pay = 100
	def amount(self):
		return  pay*(.02)
	def amount(self, weight, card):
		total = payinfo.card * weight
		return  total

}

Obj = payment()
V_category = intput()
Total = 0
If  V_category == “govt_employee”:
	personal = input(“Yes or No”)
	if personal == “Yes”
		total = obj.amount()
	else:
		print(“Nothing to pay ”)
else:
V_type = input()
C_type = input()
V_weight = input()
Total = obj.amount(v_weight, c_type)
Print(total)
