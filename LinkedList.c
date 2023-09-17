#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} node;

node* insertFirst(node* head, int data);
node* insertLast(node* head, int data);
node* insertAt(node* head, int pos, int data); 
node* deleteFirst(node* head);
node* deleteLast(node* head);
node* deleteAt(node* head, int pos); 
void showList(node* head);
int getLength(node* head);

int main() {
    node* head = NULL;
    head = insertFirst(head, 20);
    head = insertLast(head, 30);
    head = insertLast(head, 40);
    showList(head);
    printf("\n");
    head = deleteFirst(head);
    showList(head);
    printf("\n");
    // head = deleteLast(head);
    head = insertAt(head, 1, 35);
    showList(head);
    printf("\n");
    head = deleteAt(head, 1); 
    showList(head);
    getLength(head);
}

node* insertFirst(node* head, int data) {
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = data;
    newNode->next = head;
    return newNode;   
}

node* insertLast(node* head, int data) {
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = data;
    if (head == NULL) {
        newNode->next = head;
        return newNode;   
    }
    else {
        node* curr = head;
        while (curr->next != NULL) {
            curr = curr->next;
        }
        newNode->next = curr->next;
        curr->next = newNode;
        return head;
    }
}

node* insertAt(node* head, int pos, int data) {
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = data;
    // 노드가 비어있을 때
    if (head == NULL) {
        printf("리스트가 비었습니다.");
        return 0;
        // return
    }
    // pos 범위 
    if (pos >= getLength(head)) {
        printf("out of index\n");
    }
    // 첫 번째 노드에 추가
    if (pos == 0) {
        newNode->next = head;
        head = newNode;
    }
    else {
        node* curr = head;
        for (int i = 0; i < pos - 1; i++) {
            curr = curr->next;
        }
        newNode->next = curr->next;
        curr->next = newNode;
    }
    return head;
}

node* deleteFirst(node* head) {
    if (head == NULL) {
        printf("데이터가 없습니다.\n");
    }
    else {
        node* next = head->next;
        head = NULL;
        head = next;
    }
    return head;
}

node* deleteLast(node* head) {
    if (head == NULL) {
        printf("데이터가 없습니다.\n");
    }
    else {
        // remove 앞 노드 찾기
        node* curr = head;
        while (curr->next->next != NULL) {
            curr = curr->next;
        }
        curr->next = NULL;
    }
    return head;
}

node* deleteAt(node* head, int pos) {
    // 노드가 비어있을 때
    if (head == NULL) {
        printf("데이터가 없습니다.");
        return 0;
    }
    // pos 범위 
    if (pos >= getLength(head)) {
        printf("out of index\n");
    }
    if (pos == 0) {
        node* next = head->next;
        head->next = NULL;
        head = next;
    }
    else {
        node* curr = head;
        for (int i = 0; i < pos - 1; i++) {
            curr = curr->next;
        }
        node* remove = curr->next;
        curr->next = remove->next;
    }
    return head;
}

void showList(node* head) {
    if (head == NULL) {
        printf("데이터가 없습니다.");
    }
    else {
        node* curr = head;
        while (curr != NULL) {
            printf("%d ", curr->data);
            curr = curr->next;
        }
    }
}

int getLength(node* head) {
    if (head == NULL) {
        return 0;
    }
    int cnt = 1;   
    node* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
        cnt += 1;
    }
    return cnt;
}