import Image from "next/image";

export default function PainPoint() {
  return (
    <section className="w-full h-screen border-gray-700">
      <div className="top_grids w-full flex items-center">
        <div className="one w-1/7 h-20 border-b border-r border-dashed border-gray-500"></div>
        <div className="two w-5/7 h-20 border-b border-dashed  border-gray-500"></div>
        <div className="three w-1/7 h-20 border-b border-l border-dashed border-gray-500"></div>
      </div>
      <div className="mid_grids w-full flex items-center">
        <div className="left_grid w-1/7 h-100 border-b border-r border-dashed border-gray-500"></div>
        <div className="mid_grid w-5/7 h-100 border-b border-dashed border-gray-500">
          <div className="w-full pain-point flex items-center justify-center gap-x-20 p-10 ">
            <div className="left ">
              <h2 className="text-4xl mb-2">
                You think your website is safe. <br /> Actually it's the mere
                opposite.
              </h2>
              <p className="text-lg text-gray-400">
                don't you think there was an easy solution ?
              </p>
            </div>

            <div className="right">
              <Image
                src={"/assets/mock_one.png"}
                alt="mock_one"
                width={500}
                height={500}
              />
            </div>
          </div>
        </div>
        <div className="right_grid w-1/7 h-100 border-b border-l border-dashed border-gray-500"></div>
      </div>
      <div className="bottom_grids w-full flex items-center">
        <div className="left_grid w-1/7 h-20 border-t border-r border-dashed border-gray-500"></div>
        <div className="mid_grid w-5/7 h-20 border-t border-dashed border-gray-500"></div>
        <div className="right_grid w-1/7 h-20 border-t border-l border-dashed border-gray-500"></div>
      </div>
    </section>
  );
}
