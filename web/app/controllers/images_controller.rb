class ImagesController < ApplicationController
  def upload
  end

  def show_results
    resp = Faraday.post(
      'http://api',
      {image: image_b64}.to_json,
      "Content-Type" => "application/json"
    )
    @json = JSON.load(resp.body)
  end

  private

  def image_b64
    Base64.encode64(
      params[:image].tempfile.open.read.force_encoding(Encoding::UTF_8)
    )
  end
end
