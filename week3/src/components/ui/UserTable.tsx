"use client";

import Image from "next/image";


const users = [
  {
    id: 1,
    name: "John Doe",
    username: "johndoe",
    email: "john.doe@example.com",
    role: "Admin",
    status: "Active",
    joined: "Jan 2024",
    avatar: "https://i.pravatar.cc/150?img=1",
    createdAt:"18/10/2025 05:27",
    updatedAt:"18/10/2025 05:55"
  },
  {
    id: 2,
    name: "Jane Smith",
    username: "janesmith",
    email: "jane.smith@example.com",
    role: "Editor",
    status: "Pending",
    joined: "Feb 2024",
    avatar: "https://i.pravatar.cc/150?img=5",
    createdAt:"18/10/2025 05:55",
    updatedAt:"18/10/2025 06:37"
  },
    {
    id: 3,
    name: "John Doe",
    username: "johndoe",
    email: "john.doe@example.com",
    role: "Admin",
    status: "Active",
    joined: "Jan 2024",
    avatar: "https://i.pravatar.cc/150?img=1",
    createdAt:"18/10/2025 05:27",
    updatedAt:"18/10/2025 05:55"
  },
  {
    id: 4,
    name: "Jane Smith",
    username: "janesmith",
    email: "jane.smith@example.com",
    role: "Editor",
    status: "Pending",
    joined: "Feb 2024",
    avatar: "https://i.pravatar.cc/150?img=5",
    createdAt:"18/10/2025 05:55",
    updatedAt:"18/10/2025 06:37"
  },
    {
    id: 5,
    name: "John Doe",
    username: "johndoe",
    email: "john.doe@example.com",
    role: "Admin",
    status: "Active",
    joined: "Jan 2024",
    avatar: "https://i.pravatar.cc/150?img=1",
    createdAt:"18/10/2025 05:27",
    updatedAt:"18/10/2025 05:55"
  },
  {
    id: 6,
    name: "Jane Smith",
    username: "janesmith",
    email: "jane.smith@example.com",
    role: "Editor",
    status: "Pending",
    joined: "Feb 2024",
    avatar: "https://i.pravatar.cc/150?img=5",
    createdAt:"18/10/2025 05:55",
    updatedAt:"18/10/2025 06:37"
  },
    {
    id: 7,
    name: "John Doe",
    username: "johndoe",
    email: "john.doe@example.com",
    role: "Admin",
    status: "Active",
    joined: "Jan 2024",
    avatar: "https://i.pravatar.cc/150?img=1",
    createdAt:"18/10/2025 05:27",
    updatedAt:"18/10/2025 05:55"
  },
  {
    id: 8,
    name: "Jane Smith",
    username: "janesmith",
    email: "jane.smith@example.com",
    role: "Editor",
    status: "Pending",
    joined: "Feb 2024",
    avatar: "https://i.pravatar.cc/150?img=5",
    createdAt:"18/10/2025 05:55",
    updatedAt:"18/10/2025 06:37"
  }
];

export default function UserTable() {
  return (
    <div className="bg-white shadow-md rounded-lg overflow-x-auto p-4 mt-6   ">
      <table className="min-w-full divide-y divide-gray-200">
        {/* Header */}
        <thead className="bg-gray-50">
          <tr>
            <th className="px-4 py-3">
              <input type="checkbox" className="h-4 w-4 text-indigo-600" />
            </th>

            <th className=" text-left px-4 py-3 text-gray-600 text-sm font-semibold">User</th>
            <th className="text-left px-4 py-3 text-gray-600 text-sm font-semibold">Email</th>
            <th className="text-left px-4 py-3 text-gray-600 text-sm font-semibold">Role</th>
            <th className="text-left px-4 py-3 text-gray-600 text-sm font-semibold">Status</th>
            <th className="text-left px-4 py-3 text-gray-600 text-sm font-semibold">created At</th>
            <th className="text-left px-4 py-3 text-gray-600 text-sm font-semibold">updated At</th>
            
            <th className="px-4 py-3"></th>
          </tr>
        </thead>

       
        <tbody className="divide-y divide-gray-200 bg-white">
          {users.map((user) => (
            <tr key={user.id} className="hover:bg-gray-50 transition">
              {/* Checkbox */}
              <td className="px-4 py-4">
                <input type="checkbox" className="h-4 w-4 text-indigo-600" />
              </td>

          
              <td className=" px-4 py-4 flex items-center gap-3">
                <Image
                  src={user.avatar}
                  alt="Avatar"
                  width={40}
                  height={40}
                  className="rounded-full"
                />
                <div>
                  <div className="font-semibold text-gray-900">{user.name}</div>
                  <div className="text-gray-500 text-sm">{user.username}</div>
                </div>
              </td>

            
              <td className="  px-4 py-4">
                <div className="text-gray-900 text-sm">{user.email}</div>
                <div className="text-gray-500 text-xs">Joined {user.joined}</div>
              </td>

            
              <td className="px-4 py-4 text-sm text-gray-800">{user.role}</td>

             
              <td className="px-4 py-4">
                <span
                  className={`px-2 py-1 rounded-full text-xs font-semibold ${
                    user.status === "Active"
                      ? "bg-green-100 text-green-700"
                      : "bg-yellow-100 text-yellow-700"
                  }`}
                >
                  {user.status}
                </span>
              </td>


              <td className="px-4 py-4 text-sm text-gray-800">{user.createdAt}</td>
               <td className="px-4 py-4 text-sm text-gray-800">{user.updatedAt}</td>

             
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
