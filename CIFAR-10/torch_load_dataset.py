import torchvision
import torchvision.transforms as transforms

# 数据预处理
transform = transforms.Compose([
        transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])

# 加载数据集
trainset = torchvision.datasets.CIFAR10(root='/home/qingbao/Data/Dataset/CIFAR10', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True)

# testset = torchvision.datasets.CIFAR10(root='/home/qingbao/Data/Dataset/CIFAR10', train=False, download=True, transform=transform)
# testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False)
