/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * read_mmap_segment.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * new_simple_test is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * new_simple_test is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "mmap_segment.h"

int read_mmap_segment(const char *storage_id, void *buffer)
{
    //////////////////////////////////////////////////////////////////////////
    /// Checks if the storage id pointer is valid
    if (storage_id == NULL)
    {
        perror("Invalid storage id pointer provided.");
        return MMAP_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Checks if the buffer pointer is valid
    if (buffer == NULL)
    {
        perror("Invalid buffer pointer provided.");
        return MMAP_ERROR;
    }

	//////////////////////////////////////////////////////////////////////////
    /// Trys to open shared memory segment
	int fd = shm_open(storage_id, O_RDONLY, S_IRUSR | S_IWUSR);

	//////////////////////////////////////////////////////////////////////////
    /// Checks if the shared memory descriptor is valid
	if (fd == -1)
	{
		perror("Failed to open shared memory segment.");
		return MMAP_ERROR;
	}

	//////////////////////////////////////////////////////////////////////////
	/// Map shared memory segment to process address space
	void *memory = mmap(NULL, MMAP_STORAGE_SIZE, PROT_READ, MAP_SHARED, fd, 0);

	//////////////////////////////////////////////////////////////////////////
	/// Checks is mapping operation failed
	if (memory == MAP_FAILED)
	{
		perror("Failed to map memory segment.");
		close(fd);
		return MMAP_ERROR;
	}

	//////////////////////////////////////////////////////////////////////////
	/// Copy data from shared memory segment (limit MMAP_STORAGE_SIZE)
	memcpy(buffer, memory, MMAP_STORAGE_SIZE);

    //////////////////////////////////////////////////////////////////////////
    /// Unmap shared memory segment from process address space
    if (munmap(memory, MMAP_STORAGE_SIZE) == -1)
    {
        perror("Failed to unmap shared memory segment.");
        close(fd);  // Close file descriptor even if munmap fails
        return MMAP_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Close file descriptor for shared memory segment
    if (close(fd) == -1)
    {
        perror("Failed to close shared memory segment.");
        return MMAP_ERROR;
    }

    //////////////////////////////////////////////////////////////////////////
    /// Unlink shared memory after successful read and cleanup
    if (shm_unlink(storage_id) == -1)
    {
        perror("Failed to unlink shared memory segment.");
        return MMAP_ERROR;
    }

	return MMAP_SUCCESS;
}

