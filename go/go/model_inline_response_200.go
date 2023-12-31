/*
 * EazyShop Products APIs Definition
 *
 * # About Us **EazyShop** is a open market product selling company. Any website can list our products by  using our _APIs_. Shipping & other logistics will be taken care by us. You will get an `Affiliate commision` for selling our products. # Categories suported   - Mobiles     - Apple     - Samsung     - OnePlus   - Laptops   - Televisions   - Headphones 
 *
 * API version: 0.0.1
 * Contact: support@eazyshop.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type InlineResponse200 struct {

	OrderId int32 `json:"orderId,omitempty"`

	Products []Product `json:"products,omitempty"`

	Address *Address `json:"address,omitempty"`
}
