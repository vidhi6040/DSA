#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

typedef struct Node
{
    int data;
    struct Node *next;
}NODE;

class LinkedList
{
    private:
        NODE *start;
    public:
        LinkedList()
        {
            this->start = NULL;
        }
        void create()
        {
            char ch = 'y';
            NODE *new_node = NULL;
            NODE *temp = NULL;
            do
            {
                new_node = new NODE();
                new_node->next = NULL;
                printf("\nEnter Data: ");
                scanf("%d", &new_node->data);
                if(this->start == NULL)
                {
                    this->start = new_node;
                }
                else
                {
                    temp = this->start;
                    while(temp->next !=  NULL)
                    {
                        temp = temp->next;
                    }
                    temp->next = new_node;
                }
                printf("\nDo you want to add more data [y/n]?...");
                scanf(" %c", &ch);
            }while(ch == 'y');
        }
        void disp()
        {
            NODE *temp = NULL;
            if(start == NULL)
            {
                printf("\nEmpty List");
            }
            else
            {
                temp = this->start;
                printf("\nSTART -> ");
                while(temp != NULL)
                {
                    printf("%d -> ", temp->data);
                    temp = temp->next;
                }
                printf("END");
            }
        }
};

int main()
{
    LinkedList p;
    p.create();
    p.disp();
    return 0;
}