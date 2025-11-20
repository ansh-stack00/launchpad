import React from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen max-h-screen flex flex-col  ">
      <Navbar classes="w-full "/>

      <div className="flex ">
        <Sidebar />

        <main className=" p-4">
          {children}
        </main>
      </div>
    </div>
  );
}
