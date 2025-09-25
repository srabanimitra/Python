from collections import OrderedDict

# Function to manage the frame


def ref(page, capacity, frames):
    # If page is already in frames
    if page in frames:
        # Move page to front (most recent)
        frames.move_to_end(page, last=False)
    else:
        # If frame is full, remove the least recently used (last item)
        if len(frames) == capacity:
            lru, _ = frames.popitem(last=True)
            print(f"Page replaced: {lru}")
        # Insert new page at the front
        frames[page] = True
        frames.move_to_end(page, last=False)

# Function to display current frame state


def display(frames):
    print("Current frame state:", " ".join(map(str, frames.keys())))


def main():
    cap = 4  # Set capacity to 4
    frames = OrderedDict()  # Maintains order of page usage (LRU)

    # Sample page reference string
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

    # Loop through each page
    for page in pages:
        print(f"Referencing page: {page}")
        ref(page, cap, frames)
        display(frames)


if __name__ == "__main__":
    main()
