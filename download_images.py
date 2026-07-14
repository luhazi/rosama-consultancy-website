#!/usr/bin/env python3
"""
ROSAMA Consultancy — Image Downloader
Downloads 73 Africa/Tanzania-focused images from Pixabay.
Uses only Python stdlib — no pip required.
Run from inside the rosama-website/ folder:
    python3 download_images.py
"""
import os, ssl, time, urllib.request, urllib.error

BASE = os.path.join(os.path.dirname(__file__), "assets", "images")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = [
    ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    ("Referer", "https://pixabay.com/"),
    ("Accept", "image/jpeg,image/webp,image/*;q=0.8,*/*;q=0.5"),
    ("Accept-Language", "en-US,en;q=0.9"),
]

IMAGES = [
    {'url': 'https://pixabay.com/get/g18cfd76714cdf31be8d021850eec9fa485dbeb7269c21491ed8e8c555e7b19ddd16bad4011d6f8fecd9bfbe1634a01cb_1920.jpg?longlived=', 'path': 'assets/images/hero/hero-business-meeting.webp', 'title': 'Job Office', 'pid': '5382501'},
    {'url': 'https://pixabay.com/get/g8b1ba414d085f335e6ae1fc4c495e958db6c7b4ed7c5616003cffc1bee5604df23954daa411235a4096c72ab3416fa5f_1920.jpg?longlived=', 'path': 'assets/images/hero/hero-tax-consultation.webp', 'title': 'Businessman Tie', 'pid': '4782650'},
    {'url': 'https://pixabay.com/get/g8b9659686c555eb7d066713bc1f9823970d6eab280ec1aa138b48d60ce27e494f8b6b9c493df3b2a4d03d080a3e4bd41_1920.jpg?longlived=', 'path': 'assets/images/hero/hero-boardroom.webp', 'title': 'Team Executives', 'pid': '4786562'},
    {'url': 'https://pixabay.com/get/g8e04d0fba6de612b16d6234e351381360ec1cdb610d5c13a05d11f0e48310c161355c74fc5d28d1e232c87bad4dc0f09_1920.jpg?longlived=', 'path': 'assets/images/hero/hero-accounting.webp', 'title': 'African Woman Formal Wear', 'pid': '7343703'},
    {'url': 'https://pixabay.com/get/ge4c374d07934a3569d4a325f815c24d134ebd2f3b94d47b3684ff39308b79ae0db670f8696d5eb5fbbe363b48b1d5f16_1920.jpg?longlived=', 'path': 'assets/images/hero/hero-business-growth.webp', 'title': 'Man Seated Entrepreneur', 'pid': '4455091'},
    {'url': 'https://pixabay.com/get/gae2766ffeb1cf144784163c51ee785aa5e633013e42d6672385b2870fe4229d49aaf33112fabf0f8ccbc55c00884a8ab_1920.jpg?longlived=', 'path': 'assets/images/hero/hero-consulting.webp', 'title': 'Black Male African American Male', 'pid': '4568760'},
    {'url': 'https://pixabay.com/get/g211f26efd403d66dea51c7d0a19ec8275adb54a5b76b6d6e6f0c5eb60a11b59bac7aa7ea49883beb56201e5f19974cb3_1920.jpg?longlived=', 'path': 'assets/images/about/about-consultant.webp', 'title': 'Conference Team', 'pid': '2533871'},
    {'url': 'https://pixabay.com/get/g80768afc1330de34e8dfd2b4a2a54653d42859959b266b42d7c3c83c26e6e884e6d5d3019ca5a2b7d8c0143d364c8fab_1920.jpg?longlived=', 'path': 'assets/images/about/about-collaboration.webp', 'title': 'Action Collaborate', 'pid': '2277292'},
    {'url': 'https://pixabay.com/get/g516b8d3d2dec816045d94d77cf14c4fa06360731c683c1b4d4d152d3c48b84dc72814a1cfcb5c98657004be3aa47d9dc_1920.jpg?longlived=', 'path': 'assets/images/about/about-team.webp', 'title': 'Team Boss', 'pid': '4817006'},
    {'url': 'https://pixabay.com/get/gfcc4900f4b4de0a4dcd9dc2009aa8f28f53877d4a50fc048293867bda4aa91e599c2e7f05441d2634cc7165c8dc17972_1920.jpg?longlived=', 'path': 'assets/images/about/about-reports.webp', 'title': 'Entrepreneur Startup', 'pid': '593377'},
    {'url': 'https://pixabay.com/get/g8b1ba414d085f335e6ae1fc4c495e958db6c7b4ed7c5616003cffc1bee5604df23954daa411235a4096c72ab3416fa5f_1920.jpg?longlived=', 'path': 'assets/images/services/service-tax.webp', 'title': 'Businessman Tie', 'pid': '4782650'},
    {'url': 'https://pixabay.com/get/g887f34389848af80f5b800c13187b72ba989eff97148b77039b6cec345ab81f0765e214853db71dde98611e17e0d1eff_1920.jpg?longlived=', 'path': 'assets/images/services/service-registration.webp', 'title': 'Startup Start-Up', 'pid': '593354'},
    {'url': 'https://pixabay.com/get/g2566b0a2aac10f7751ec8f2c302d84a974d5b97dcb311f08d05f6c99cc0bb65d0c8e03b75d40a579669e8f6cb553a345_1920.jpg?longlived=', 'path': 'assets/images/services/service-accounting.webp', 'title': 'Working Female', 'pid': '791849'},
    {'url': 'https://pixabay.com/get/g62904c26511ce9812eaf4c65ba907a298d0c0f7520ab338d673f17da4d3beecfaecea95352bebcfcf8d7bd10af5bd659_1920.jpg?longlived=', 'path': 'assets/images/services/service-bookkeeping.webp', 'title': 'Man Laptop', 'pid': '593372'},
    {'url': 'https://pixabay.com/get/g52346be42407a1afa64927a7ccb6aae3183556928fb3b05f5ecd741324fc68011fe4f787a96ae0cc839615404e08ecf6_1920.jpg?longlived=', 'path': 'assets/images/services/service-payroll.webp', 'title': 'Businesswoman Office', 'pid': '4126489'},
    {'url': 'https://pixabay.com/get/gf70ebea2a4ae039624b9ea5febf4c7e91d55b753da3d938e508f5f9e8c21407db093cb6ba1b67cb45700dc36bfee5786_1920.jpg?longlived=', 'path': 'assets/images/services/service-immigration.webp', 'title': 'Friends Khartoum', 'pid': '2895745'},
    {'url': 'https://pixabay.com/get/g5d18565fa74b2b8dd67d542cebc302cfc83651dce5e075def6e2ff89f987b19ae915eb6c4d896a3a5940fcfdfad3c754_1920.jpg?longlived=', 'path': 'assets/images/services/service-advisory.webp', 'title': 'People Business', 'pid': '3912733'},
    {'url': 'https://pixabay.com/get/g214c42e2e6c248b33f337a4aaf22abd66ecf624eb6a447968473114ceddb138c3d4e03d12d1a1525c33a4c3e32276355_1920.jpg?longlived=', 'path': 'assets/images/services/service-investment.webp', 'title': 'Entrepreneur Startup', 'pid': '593353'},
    {'url': 'https://pixabay.com/get/g14400b643cee671d49ecf0ce059e5a117a35c35cf8b48ee85fa6446045fb344e8999981418a17b6577a718cb7fd140d0_1920.jpg?longlived=', 'path': 'assets/images/services/service-licensing.webp', 'title': 'Woman Business', 'pid': '8872804'},
    {'url': 'https://pixabay.com/get/g8b6f7684f4025a587d4ce1427dd9b94754e734d9fd5a123c9bd7add0ca510b2d78b48900be5785a23961aef1af993f3d_1920.jpg?longlived=', 'path': 'assets/images/services/service-secretarial.webp', 'title': 'Girl Woman', 'pid': '2583442'},
    {'url': 'https://pixabay.com/get/g2e11054e63a2668070a44a364633baf098aecdae5d33a0db18f036e04c249c55faf3476bd6f487b095d7ac4d83d54a38_1920.jpg?longlived=', 'path': 'assets/images/services/service-financial.webp', 'title': 'Businessman Consulting', 'pid': '2606509'},
    {'url': 'https://pixabay.com/get/g87f65ca541a7893a87042f0a2018e2ef8a48a1c77576123f662bcc17b816baac52fd53de42425a50ebf201fb25740b9b_1920.jpg?longlived=', 'path': 'assets/images/services/service-audit.webp', 'title': 'Coworkers Meeting', 'pid': '4156015'},
    {'url': 'https://pixabay.com/get/g07e6e16ffdc137469d7cb4a6ca9f420a04ca2c30361be03cbc914783a6d0f9a294a212ee94edc964b81403f80fe83498_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-healthcare.webp', 'title': 'Nurse Medicine', 'pid': '2019420'},
    {'url': 'https://pixabay.com/get/g7e972f176fbf73f728cff51e3c79fe956c2bace7becf2842bd6de23f07d5cfba8696fd62c95a9e0edae444382f2f2e48_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-construction.webp', 'title': 'Construction Site Engineer', 'pid': '4020496'},
    {'url': 'https://pixabay.com/get/g8ec1eb89a19f169fdb0795b7e5136afacf8b6ad7f5ecd3c503c03d6c56ce4a53e7890579eb25378645a7a4e33ba7b862_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-agriculture.webp', 'title': 'Ghana Cocoa', 'pid': '2870655'},
    {'url': 'https://pixabay.com/get/g855e6a5d6136a9a4f69704d0090b590eb21a86292c54c8dd3f26f9c7448c5e0811d0dd3d33c0c943e523baa056bc250a_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-manufacturing.webp', 'title': 'Crane Construction Site', 'pid': '7095357'},
    {'url': 'https://pixabay.com/get/g168c4db37832c3008fabd20c18d81a88a697507567eedee28900f4ad46824f36c8def01bd52e1704a043efe451e2748a_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-technology.webp', 'title': 'Entrepreneur Creativity', 'pid': '4784289'},
    {'url': 'https://pixabay.com/get/g4160ef255eec481670ad4f5b07d300c5099f19359dc273830d5f73bdc0c7062ec62d16b705aaad6e3a24c52078b8976b_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-education.webp', 'title': 'Children Of Uganda Uganda', 'pid': '2245270'},
    {'url': 'https://pixabay.com/get/g8cca2dd7f8c115c5f25b7072ebfc5040feb843ed88bde51ef1e875be52bca01e839533b107c4e5ab61eefa8a57561643_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-hospitality.webp', 'title': 'Beacon Island Resort Hotel', 'pid': '3711101'},
    {'url': 'https://pixabay.com/get/g5de536e678ebee19e0efc6a21cb569b346abebae385bd64ee3eed13cfc5ceffe57ee24117b9240a603af89f07a58e715_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-retail.webp', 'title': 'Food Vendor', 'pid': '4024200'},
    {'url': 'https://pixabay.com/get/g3aa3d6663a946cd7adbc00d80030fa9a6f62d5049b95a1144398b4935b90f4bf24de72a4e06f8b7062620181202ae700_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-transport.webp', 'title': 'Uganda Transport', 'pid': '5005579'},
    {'url': 'https://pixabay.com/get/g91c1d0d832ef97d3d873ed390b84f78f756f9b7c8d3b44d6d5b9facd0b3fd9683369eb17e1caeb110288be7d2c397d96_1920.png?longlived=', 'path': 'assets/images/industries/industry-ngo.webp', 'title': 'Hands Team', 'pid': '1917895'},
    {'url': 'https://pixabay.com/get/g7384f487fb772e610cb29bd9bc0ce6528de292e986feb4aa8544a371739af4b9d3f35e39ecfcc085d0198dc42e8caca3_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-energy.webp', 'title': 'Africa Namibia', 'pid': '139343'},
    {'url': 'https://pixabay.com/get/g44aded5d71d8cc322dae6a7eebc7465480de3d25d6ea5062f9756a149f48ae957543430fd59ab00cd7cfe3d221d462fb_1920.jpg?longlived=', 'path': 'assets/images/industries/industry-mining.webp', 'title': 'Construction Worker Crane', 'pid': '7859047'},
    {'url': 'https://pixabay.com/get/gd2faac2b95fa9f41240636e27c31bf487749739ebff87bb9339591fff8b72751bdbc72c3d1c56a3f7c161e2c5f74dfb4_1920.jpg?longlived=', 'path': 'assets/images/testimonials/testimonial-handshake.webp', 'title': 'Run Motorsport', 'pid': '4462878'},
    {'url': 'https://pixabay.com/get/g8b1ba414d085f335e6ae1fc4c495e958db6c7b4ed7c5616003cffc1bee5604df23954daa411235a4096c72ab3416fa5f_1920.jpg?longlived=', 'path': 'assets/images/testimonials/testimonial-client.webp', 'title': 'Businessman Tie', 'pid': '4782650'},
    {'url': 'https://pixabay.com/get/gede09f6c35f8ee4ce440ced19dec88e45c3553f231f00ee3ed9ae84c62acb3aa1b1728da9959660eb839c14946eb846f_1920.jpg?longlived=', 'path': 'assets/images/testimonials/testimonial-meeting.webp', 'title': 'Chairs Conference Room', 'pid': '2181919'},
    {'url': 'https://pixabay.com/get/gb99f917e794003d0596908f3128fa8fe27dd1f9742e9ddbbba8bfb2656812f18ac8e9a62c1657b677c7decaad01cc4e6_1920.jpg?longlived=', 'path': 'assets/images/testimonials/testimonial-conference.webp', 'title': 'Tuscany Autodepoca', 'pid': '2771661'},
    {'url': 'https://pixabay.com/get/gae971929d144935449fdc364a0fbbb884126cf776200b0bb96e8b9ca7ee0940454b1273b9a4427f655d0d38b2c249fc9_1920.jpg?longlived=', 'path': 'assets/images/testimonials/testimonial-background.webp', 'title': 'Job Office', 'pid': '5382501'},
    {'url': 'https://pixabay.com/get/g8b1ba414d085f335e6ae1fc4c495e958db6c7b4ed7c5616003cffc1bee5604df23954daa411235a4096c72ab3416fa5f_1920.jpg?longlived=', 'path': 'assets/images/team/team-consultant.webp', 'title': 'Businessman Tie', 'pid': '4782650'},
    {'url': 'https://pixabay.com/get/g8b9659686c555eb7d066713bc1f9823970d6eab280ec1aa138b48d60ce27e494f8b6b9c493df3b2a4d03d080a3e4bd41_1920.jpg?longlived=', 'path': 'assets/images/team/team-executives.webp', 'title': 'Team Executives', 'pid': '4786562'},
    {'url': 'https://pixabay.com/get/g8e04d0fba6de612b16d6234e351381360ec1cdb610d5c13a05d11f0e48310c161355c74fc5d28d1e232c87bad4dc0f09_1920.jpg?longlived=', 'path': 'assets/images/team/team-reception.webp', 'title': 'African Woman Formal Wear', 'pid': '7343703'},
    {'url': 'https://pixabay.com/get/gae2766ffeb1cf144784163c51ee785aa5e633013e42d6672385b2870fe4229d49aaf33112fabf0f8ccbc55c00884a8ab_1920.jpg?longlived=', 'path': 'assets/images/team/team-portrait.webp', 'title': 'Black Male African American Male', 'pid': '4568760'},
    {'url': 'https://pixabay.com/get/g52d641f3d949c3815e2b4f6d22b7c5f2e0ec5812fc8f1a4c10b905d6a1dccef8f392664098dcb6410ca91a60a9783920_1920.jpg?longlived=', 'path': 'assets/images/team/team-office.webp', 'title': 'Startup Start-Up', 'pid': '593341'},
    {'url': 'https://pixabay.com/get/gca222171dd86f34d732f0d4b9e75b6531ac933133de64b3de2dfd903c400700f0dd2394ab3e7ce58762ce0eda93a13ca_1920.jpg?longlived=', 'path': 'assets/images/cta/cta-handshake.webp', 'title': 'Video Conference Home Office', 'pid': '10318099'},
    {'url': 'https://pixabay.com/get/gc8c7b3861e6991b749447aa930545d7e9c3d82c2ce2dacfeb9054b02940b56085fc22e29f6065315121627f7441c83ba_1920.jpg?longlived=', 'path': 'assets/images/cta/cta-contracts.webp', 'title': 'Whiteboard Man', 'pid': '849813'},
    {'url': 'https://pixabay.com/get/gdf3d094df96c0f117a62fe7de02eaa14ebdc80f2bc527e424b1f1e857a842fa8d23f39c8cbd94a52e6bfa02bc618700f_1920.jpg?longlived=', 'path': 'assets/images/cta/cta-success.webp', 'title': 'Business Woman Freelancer', 'pid': '7642552'},
    {'url': 'https://pixabay.com/get/gb82efacc8fce3abe6394bcccf330e1f69e21fd24feb2270d61cc1d904c8121110ba2ba4ba4b2f0fbf363589c1fcf4569_1920.jpg?longlived=', 'path': 'assets/images/cta/cta-skyline.webp', 'title': 'Cape Town South Africa', 'pid': '997517'},
    {'url': 'https://pixabay.com/get/g168c4db37832c3008fabd20c18d81a88a697507567eedee28900f4ad46824f36c8def01bd52e1704a043efe451e2748a_1920.jpg?longlived=', 'path': 'assets/images/cta/cta-growth.webp', 'title': 'Entrepreneur Creativity', 'pid': '4784289'},
    {'url': 'https://pixabay.com/get/g4488caba84f2ce9147eb2be7f87e10558901d025591c94ac3be876b082aa6bea8685a511f20002e60bef6022accc8eeb_1920.jpg?longlived=', 'path': 'assets/images/cta/cta-business.webp', 'title': 'Laptops Meeting', 'pid': '593296'},
    {'url': 'https://pixabay.com/get/g8723ad9449e96c37828b1b9d49282f99549f1be88a34358177c1af4d7f72e4f0dec272b3422365664fcd500e1835ab83_1920.jpg?longlived=', 'path': 'assets/images/contact/contact-reception.webp', 'title': 'Job Office', 'pid': '5382501'},
    {'url': 'https://pixabay.com/get/g5c6fecfaaa95a52a57dc7f786dd392fbd43596f86835a3bfe2840c87410fe98218f0f99ed416aaefa6b17b352292d46b_1920.jpg?longlived=', 'path': 'assets/images/contact/contact-building.webp', 'title': 'Africa Architecture', 'pid': '4372120'},
    {'url': 'https://pixabay.com/get/g1eb2bc07cfce6ef56c938a3874d70bfe7fd70f4222d58599f2cf590440c2d333b91d4ff8b3e714bcb0fbfa194f00887f_1920.jpg?longlived=', 'path': 'assets/images/contact/contact-workspace.webp', 'title': 'Office Space Office', 'pid': '1744805'},
    {'url': 'https://pixabay.com/get/g9a22cc901b087a5e29259eba9cf3b7cf00c83bf14343f7628b5dfedb2961f547c4373c8a1e8f78fe23e1f84b66b96d1b_1920.jpg?longlived=', 'path': 'assets/images/contact/contact-conference.webp', 'title': 'Startup Start-Up', 'pid': '593341'},
    {'url': 'https://pixabay.com/get/g07181361b2dfd54a8ac92d3bbe7dc561e3f4b44557d3d669511e64caf2b83f66c7427a015b222a69da4198ff946286b9_1920.jpg?longlived=', 'path': 'assets/images/contact/contact-entrance.webp', 'title': 'City Cityscape', 'pid': '3143632'},
    {'url': 'https://pixabay.com/get/g6c2d7580aa2891a49d5fa22574d78040a2e90b1042fdbd9ea79245f5e8301a81ad035a545c215a0a23104dcfc99596be_1920.jpg?longlived=', 'path': 'assets/images/contact/contact-district.webp', 'title': 'Kenya Africa', 'pid': '328861'},
    {'url': 'https://pixabay.com/get/gb448c0c971edfb5b6723de1ada709c11037adb4660417721387d2de1025d24e606863bdc47215619ce10e4e50af392ef_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-tax-planning.webp', 'title': 'Fashion Male', 'pid': '4951639'},
    {'url': 'https://pixabay.com/get/g2566b0a2aac10f7751ec8f2c302d84a974d5b97dcb311f08d05f6c99cc0bb65d0c8e03b75d40a579669e8f6cb553a345_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-accounting.webp', 'title': 'Working Female', 'pid': '791849'},
    {'url': 'https://pixabay.com/get/ge4c374d07934a3569d4a325f815c24d134ebd2f3b94d47b3684ff39308b79ae0db670f8696d5eb5fbbe363b48b1d5f16_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-registration.webp', 'title': 'Man Seated Entrepreneur', 'pid': '4455091'},
    {'url': 'https://pixabay.com/get/g45e1443a0922ffb517480540cc22bca76c6117bf9648ccbf68012f41a75acc227735d24d1166163cada5c719399c6e59_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-governance.webp', 'title': 'Meeting Business', 'pid': '2284501'},
    {'url': 'https://pixabay.com/get/gfcc4900f4b4de0a4dcd9dc2009aa8f28f53877d4a50fc048293867bda4aa91e599c2e7f05441d2634cc7165c8dc17972_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-reports.webp', 'title': 'Entrepreneur Startup', 'pid': '593377'},
    {'url': 'https://pixabay.com/get/g214c42e2e6c248b33f337a4aaf22abd66ecf624eb6a447968473114ceddb138c3d4e03d12d1a1525c33a4c3e32276355_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-investment.webp', 'title': 'Entrepreneur Startup', 'pid': '593353'},
    {'url': 'https://pixabay.com/get/g2ce42bd3c9d190028814a38005d896e5342f5a1a40837bf93f1aa579e8bc1ffc826e0b70ecb0cf5a2c09dda655c49536_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-entrepreneurship.webp', 'title': 'Startup Business', 'pid': '849804'},
    {'url': 'https://pixabay.com/get/gc945d356d6aabaf8c4db76a91c76a9cff3a0e71455ba70a0360dd11747c2ac2e19badcd4385ae00d85a6c3849e4bf124_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-economic.webp', 'title': 'Egypt Luxor', 'pid': '490'},
    {'url': 'https://pixabay.com/get/g6cc360881847320bb2508c23efcf29a2ce9e8257a21c1cd3f7431b357f23ec3a00ff6388d7b4aff1c3f3034ae2a57e9e_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-sme.webp', 'title': 'Gambia Market', 'pid': '239849'},
    {'url': 'https://pixabay.com/get/g168c4db37832c3008fabd20c18d81a88a697507567eedee28900f4ad46824f36c8def01bd52e1704a043efe451e2748a_1920.jpg?longlived=', 'path': 'assets/images/blog/blog-technology.webp', 'title': 'Entrepreneur Creativity', 'pid': '4784289'},
    {'url': 'https://pixabay.com/get/gd7ce5d443178754b8244db37a181d8278675015ae97a93e204f291cf39778ee0f2fb4857bfd086a56d41b4e7978e36c4_1920.jpg?longlived=', 'path': 'assets/images/backgrounds/bg-hero-overlay.webp', 'title': 'Table Mountain Cape Town City Bowl', 'pid': '3597002'},
    {'url': 'https://pixabay.com/get/g6c2d7580aa2891a49d5fa22574d78040a2e90b1042fdbd9ea79245f5e8301a81ad035a545c215a0a23104dcfc99596be_1920.jpg?longlived=', 'path': 'assets/images/backgrounds/bg-stats.webp', 'title': 'Kenya Africa', 'pid': '328861'},
    {'url': 'https://pixabay.com/get/gb82efacc8fce3abe6394bcccf330e1f69e21fd24feb2270d61cc1d904c8121110ba2ba4ba4b2f0fbf363589c1fcf4569_1920.jpg?longlived=', 'path': 'assets/images/backgrounds/bg-cta.webp', 'title': 'Cape Town South Africa', 'pid': '997517'},
    {'url': 'https://pixabay.com/get/gae971929d144935449fdc364a0fbbb884126cf776200b0bb96e8b9ca7ee0940454b1273b9a4427f655d0d38b2c249fc9_1920.jpg?longlived=', 'path': 'assets/images/office/office-main.webp', 'title': 'Job Office', 'pid': '5382501'},
    {'url': 'https://pixabay.com/get/g18cfd76714cdf31be8d021850eec9fa485dbeb7269c21491ed8e8c555e7b19ddd16bad4011d6f8fecd9bfbe1634a01cb_1920.jpg?longlived=', 'path': 'assets/images/office/office-boardroom.webp', 'title': 'Job Office', 'pid': '5382501'},
    {'url': 'https://pixabay.com/get/ga4b82b0d319bbe9dc523a8e51f2658a556a728554b2a5a3542be6af5f3e9446559eccd15010dfc1db7109cca3dc28eca_1920.jpg?longlived=', 'path': 'assets/images/office/office-workspace.webp', 'title': 'Chairs Furniture', 'pid': '7951845'},
    {'url': 'https://pixabay.com/get/g5c0c640a55c0eeaf6bc39369b562df9ca649bccfc120ed224f3b104e609418291f8a2106b4f868d5afab547be76cff3a_1920.jpg?longlived=', 'path': 'assets/images/office/office-reception.webp', 'title': 'Building Architecture', 'pid': '4884852'},
]

def download(entry):
    url  = entry['url']
    path = os.path.join(BASE, *entry['path'].replace("assets/images/","").split("/"))
    title = entry['title']

    if not url:
        print(f"  [SKIP] no URL — {title}")
        return False

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save as .jpg (strip .webp extension from path)
    if path.endswith('.webp'):
        path = path[:-5] + '.jpg'

    if os.path.exists(path):
        print(f"  [OK]   exists — {title}")
        return True

    req = urllib.request.Request(url, headers=dict(HEADERS))
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
            data = resp.read()
        with open(path, 'wb') as f:
            f.write(data)
        kb = len(data) // 1024
        print(f"  [DL]   {kb:4d} KB — {title}")
        return True
    except urllib.error.HTTPError as e:
        print(f"  [ERR]  HTTP {e.code} — {title}")
    except urllib.error.URLError as e:
        print(f"  [ERR]  {e.reason} — {title}")
    except Exception as e:
        print(f"  [ERR]  {e} — {title}")
    return False

def main():
    print(f"\nROSAMA Image Downloader — {len(IMAGES)} images\n")
    ok = skip = err = 0
    for i, img in enumerate(IMAGES, 1):
        print(f"[{i:02d}/{len(IMAGES)}] ", end="")
        result = download(img)
        if img['url'] == '':
            skip += 1
        elif result:
            ok += 1
        else:
            err += 1
        time.sleep(0.4)   # polite delay

    print(f"\n{'='*50}")
    print(f"Done: {ok} downloaded, {skip} skipped (no URL), {err} errors")
    print(f"Images saved to: {BASE}")

if __name__ == "__main__":
    main()
