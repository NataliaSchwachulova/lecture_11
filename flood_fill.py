import matplotlib.pyplot as plt


def flood_fill(img_num_array, x_now=0, y_now=0):
    x, y = img_num_array.shape

    plt.imshow(img_num_array, cmap="gray")
    plt.show(block=False)
    plt.pause(0.00001)
    plt.clf()

    if x_now < 0 or x_now > x-1 or y_now < 0 or y_now > y-1:
        return img_num_array

    elif img_num_array[x_now, y_now] == 0 or img_num_array[x_now, y_now] == 2:
        return img_num_array

    elif img_num_array[x_now, y_now] == 1:
        img_num_array[x_now, y_now] = 2
        return flood_fill(img_num_array, x_now-1, y_now),\
               flood_fill(img_num_array, x_now+1, y_now),\
               flood_fill(img_num_array, x_now, y_now-1),\
               flood_fill(img_num_array, x_now, y_now+1)



def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    #img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]
    #img = flood_fill(img, 0, 0)

    flood_fill(img)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
