"use client";

import { useState } from "react";
import Card from "@/components/ui/Card";
import Modal from "@/components/ui/Modal";

export default function Home() {
  const [modalOpen, setModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState("");

  const openModal = (content : string) => {
    setModalContent(content);
    setModalOpen(true);
  };

  return (
    <div className="p-10">
      <div className="flex gap-6">

        <Card
          title="Primary Card"
          colorClass="bg-blue-600"
          onViewDetails={() => openModal("This is the primary card content")}
        />

        <Card
          title="Warning Card"
          colorClass="bg-yellow-400"
          onViewDetails={() => openModal("Warning card details go here")}
        />

        <Card
          title="Success Card"
          colorClass="bg-green-600"
          onViewDetails={() => openModal("Success card extra information")}
        />

        <Card
          title="Danger Card"
          colorClass="bg-red-600"
          onViewDetails={() => openModal("Danger card critical info")}
        />

      </div>

     
      <Modal open={modalOpen} onClose={() => setModalOpen(false)}>
        {modalContent}
      </Modal>
    </div>
  );
}
