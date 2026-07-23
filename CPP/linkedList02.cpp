#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<conio.h>

using namespace std;

typedef struct Node
{
    int data;
    struct Node *next = NULL;
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
                new_node = new Node();
                new_node->next = NULL;
                printf("\nEnter Data: ");
                scanf("%d", &new_node->data);
                if(this->start == NULL)
                {
                    this->start = new_node;
                }
                else
                {
                    temp = start;
                    while(temp->next != NULL)
                    {
                        temp = temp->next;
                    }
                    temp->next = new_node;
                }
                printf("\nDo you want more data [y/n]?...");
                scanf(" %c", &ch);
            } while (ch == 'y');
        }
        void disp()
        {
            NODE *temp = NULL;
            if(this->start == NULL)
            {
                printf("\nNo elements found");
            }
            temp = start;
            printf("\nSTART -> ");
            while(temp != NULL)
            {
                printf("%d -> ", temp->data);
                temp = temp->next;
            }
            printf("END");
        }
        void add(int data)
        {
            NODE *new_node = new Node();
            new_node->data = data;
            new_node->next = NULL;
            if(start == NULL)
            {
                start = new_node;
            }
            else
            {
                NODE *temp = start;
                while (temp->next != NULL)
                {
                    temp = temp->next;
                }
                temp->next = new_node;
            }
        }
        void insert(int data, string pos, int index)
        {
            NODE *new_node = new Node();
            new_node->next = NULL;
            new_node->data = data;   
            if (pos == "first")
            {
                if (this->start == NULL)
                {
                    this->start = new_node;
                }
                else
                {
                    new_node->next = this->start;
                    this->start = new_node;
                }
            }
            else if (pos == "last")
            {
                if (this->start == NULL)
                {
                    this->start = new_node;
                }
                else
                {
                    NODE *temp = start;
                    while (temp->next != NULL)
                    {
                        temp = temp->next;
                    }
                    temp->next = new_node;
                }
            }
            else if (pos == "any")
            {
                if (this->start == NULL)
                {
                    this->start = new_node;
                }
                else
                {
                    NODE *temp = start;
                    int i=0;
                    while (i < index-1)
                    {
                        temp = temp->next;
                        i++;
                    }
                    new_node->next = temp->next;
                    temp->next = new_node;
                }
            }
            else
            {
                printf("Invalid Position");
            }
        }
        void count()
        {
            Node *temp = start;
            int c = 0;
            while(temp != NULL)
            {
                temp = temp->next;
                c++;
            }
            printf("Number of elements: %d", c);
        }
};
int main()
{
    LinkedList p;
    p.create();
    p.add(10);
    p.insert(100, "first", 0);
    p.insert(300, "last", 0);
    p.insert(150, "any", 2);
    p.count();
    p.disp();
    return 0;
}