#include <python.h>
#define _POSIX_C_SOURCE 199309L
/**
 * print_python_list_info - function to print basic info about Python lists
 * @p: input pointer to PyObject or the Python list to print info about
 */

void print_python_list_info(PyObject *p)
{
	size_t len = PyList_Size(p);

	printf("[*] Size of the Python list = %d\n", len);
	printf("[*] Allocated = %d\n", object->allocated);
	for (i = 0, i < len; i++)
		printf("Element %d: %s\n", i, "str");
}
