import React from "react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    // <div className="min-h-screen max-h-screen flex flex-col  ">
    //   <Navbar classes="w-full "/>

    //   <div className="flex ">
    //     <Sidebar />

        // <main className=" p-4">
        //   {children}
        // </main>
    //   </div>
    // </div>
    <>
   <div className="w-screen h-screen flex items-center justify-center ">
        <main className="bg-amber-50 transition-opacity shadow-2xl border-amber-50 w-[50%] h-[70%] rounded-3xl font-black text-gray-950">
            {children}
        </main>
   </div>
    </>
  );
  
}
